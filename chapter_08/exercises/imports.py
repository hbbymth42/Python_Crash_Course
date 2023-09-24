import user_profile 

print(user_profile.build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics'))

from user_profile import build_profile

print(build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics'))

from user_profile import build_profile as bp

print(bp('albert', 'einstein',
                             location='princeton',
                             field='physics'))

import user_profile as up

print(up.build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics'))

from user_profile import *

print(build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics'))