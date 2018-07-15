>>> from ydk.services import CRUDService
>>> from ydk.providers import NetconfServiceProvider
>>> from ydk.models.openconfig import bgp
>>> provider = NetconfServiceProvider(address='xrv', port=830, username="cisco", password="cisco", protocol="ssh")
>>> crud = CRUDService()
>>> bgp = bgp.Bgp()
>>> bgp.global_.config.as_ = 65512
>>> crud.create(provider, bgp)
>>>


RP/0/0/CPU0:xrv# show run | begin bgp
Wed Aug 24 19:27:22.111 UTC
Building configuration...
router bgp 65512
!

>>> bgp.global_.config.router_id = '1.1.1.1'
>>> crud.create(provider, bgp)


# test validation
>>> bgp.global_.config.as_ = -1
>>>
>>> crud.create(provider, bgp)


Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/ydk/services/crud_service.py", line 61, in create
    self._execute_crud_operation_on_provider(provider, entity, 'CREATE', False)
  File "/usr/local/lib/p
