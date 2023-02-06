# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Camillo Rossi (@camrossi) <camrossi@cisco.com>
# Simplified BSD License (see licenses/simplified_bsd.txt or https://opensource.org/licenses/BSD-2-Clause)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: nd_pcv_compliance
version_added: "0.2.0"
short_description: Query pre-change validation compliance
description:
- Query pre-change validation compliance on Cisco Nexus Dashboard Insights (NDI).
author:
- Cindy Zhao (@cizhao)
options:
  insights_group:
    description:
    - The name of the insights group.
    type: str
    required: yes
    aliases: [ fab_name, ig_name ]
  name:
    description:
    - The name of the pre-change validation.
    type: str
  site_name:
    description:
    - Name of the Assurance Entity.
    type: str
    aliases: [ site ]
extends_documentation_fragment: cisco.nd.modules
'''

EXAMPLES = r'''
- name: Get prechange validation compliance result
  cisco.nd.nd_pcv_compliance:
    insights_group: exampleIG
    site_name: exampleSite
    name: exampleName
  register: query_results
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.nd.plugins.module_utils.nd import NDModule, nd_argument_spec
from ansible_collections.cisco.nd.plugins.module_utils.ndi import NDI

hitcount_by_map = {
    'Epg': 'hitcountByEpgPair',
    'EpgContract': 'hitcountByEpgPairContract',
    'EpgContractFilter': 'hitcountByEpgPairContractFilter',
    'EpgTenant': 'hitcountByEpgpairTenantPair',
    'Tenant': 'hitcountByTenantPair',
    'EpgLeaf': 'hitcountByEpgPairLeaf',
    'EpgContractLeaf': 'hitcountByEpgPairContractLeaf',
    'EpgContractFilterLeaf': 'hitcountByEpgPairContractFilterLeaf',
    'EpgTenantLeaf': 'hitcountByEpgPairTenantPairLeaf',
    'TenantPairLeaf': 'hitcountByTenantPairLeaf',
}


def main():
    argument_spec = nd_argument_spec()
    argument_spec.update(
        insights_group=dict(type='str', required=True, aliases=[ "fab_name", "ig_name" ]),
        file=dict(type='str', default=""),
        site_name=dict(type='str', required=True, aliases=[ "site" ]),
        hitcount_by=dict(type='str', default="EpgContractLeaf", choices=list(hitcount_by_map.keys())),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    nd = NDModule(module)
    ndi = NDI(nd)
    file = nd.params.get('file')
    site_name = nd.params.get('site_name')
    insights_group = nd.params.get('insights_group')
    hitcount_by =  nd.params.get('hitcount_by')
    stats = ndi.get_contract_hit_stats(insights_group, site_name, hitcount_by_map[hitcount_by])
    ndi.contract_hit_stats_to_csv(file, stats)
    nd.exit_json()
if __name__ == "__main__":
    main()