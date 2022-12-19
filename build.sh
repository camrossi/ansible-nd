cd ~/ansible-nd/
ansible-galaxy collection build --force
ansible-galaxy collection install cisco-nd-* --force
cd ~/.ansible/collections/ansible_collections/cisco/nd

#ansible-test coverage erase
#ansible-test units --docker --color --truncate 0 -v --coverage

#ansible-test sanity --docker --color --truncate 0 -v --coverage

#ansible-test sanity --docker --color --truncate 0 -vvv --coverage nd_version

# ansible-test network-integration --docker --color --truncate 0 -vvvv --coverage nd_pcv_compliance

#ansible-test network-integration --docker --color --truncate 0 -vvv --coverage 
#ansible-test coverage report

# ansible-test coverage html
# open ~/.ansible/collections/ansible_collections/cisco/nd/tests/output/reports/coverage/index.html