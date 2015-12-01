#!/usr/bin/env python
import os
import sys
import time
import yaml
import argparse
import contextlib
from pprint import pprint as pp

@contextlib.contextmanager
def chdir(dir_name=None):
    cur_dir = os.getcwd()
    try:
        if dir_name is not None:
            os.chdir(dir_name)
            yield
    finally:
        os.chdir(cur_dir)


def clone_pks_repo():
    tmp_dir = '/tmp/pks-repo'

    if os.path.exists(tmp_dir):
        with chdir(dir_name=tmp_dir):
            os.system('git pull origin master')
    else:
        with chdir(dir_name='/tmp'):
            os.system('git clone %s' % args.pks_repo)


def get_all_pub_keys(tmp_dir='/tmp/pks-repo'):
    """"""
    r = []
    for a, b, c in os.walk(tmp_dir):
        for key in c:
            if key.endswith('.pub'):
                with open(os.path.join(a, key), 'r') as fp:
                    r.append(fp.read())
    return r


def update_pks_file():
    """"""
    clone_pks_repo()
    r = get_all_pub_keys()
    with open("%sroles/add_extra_pk/files/pubkeys.pub" % args.project_root, 'w' ) as fp:
        fp.writelines(r)


def replace_group_vars_with_actual_values():
    with open("%sgroup_vars/all.tpl" % args.project_root, 'r') as fp:
        t = list(yaml.load_all(fp))
        t[0]["ssh_user_name"] = args.ssh_user_name
        t[0]["qeos_vm_name"] = name_tpl
        t[0]["rhevm_base_url"] = t[0]["rhevm_base_url"] % (args.rhevm_ver, args.rhel_ver[:-1])
        t[0]["rhevm_ver"] = t[0]["rhevm_ver"] % (args.rhevm_ver[:2], args.rhevm_ver[2:])
        t[0]["qeos_image_id"] = t[0]["qeos_image_list"][args.image_id][0]
        t[0]["qeos_image_name"] = t[0]["qeos_image_list"][args.image_id][1]

    with open("%sgroup_vars/all" % args.project_root, 'w') as fp2:
        yaml.dump_all(t, fp2,
            default_style='"',
            default_flow_style=False,
            indent=2,
            explicit_start=True)


if __name__ == '__main__':
    """"""
    parser = argparse.ArgumentParser(description='Replace some vars group_vars/all')
    parser.add_argument('-sn', dest='ssh_user_name', default='cloud-user', help='ssh_user_name used to connect to the qeos instance')
    parser.add_argument('-v1', dest='rhevm_ver', default='vt15', help='rhevm version e.g.: vt14, vt15')
    parser.add_argument('-v2', dest='rhel_ver', default='el66', help='rhel version e.g.: el66, el71')
    parser.add_argument('-pr', dest='project_root', default='', help='absolut path of project root')
    parser.add_argument('-pks', dest='pks_repo', default='git@10.8.48.252:yaniwang/pks-repo.git', help='The git repo hold all ssh public-keys')
    parser.add_argument('-imgid', dest='image_id', type=int, choices=[0, 1, 2,], default=2, help='select the desired image id 0 -> 7.1, 1 > 6.7, 2 -> 6.6')
    args = parser.parse_args()

    prefix = "DoNotTouch__RHEVM"
    suffix = time.strftime("%Y%m%d%H%M")
    name_tpl = "{prefix}_{rhevm_ver}_{rhel_ver}_{suffix}".format(prefix=prefix,
                                                                 rhevm_ver=args.rhevm_ver,
                                                                 rhel_ver=args.rhel_ver,
                                                                 suffix=suffix)

    update_pks_file()
    replace_group_vars_with_actual_values()
