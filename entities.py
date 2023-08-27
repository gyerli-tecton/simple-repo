from tecton import Entity

user = Entity(
    name='user',
    join_keys=['user_id'],
    description='A user of the platform',
    owner='gursoy@tecton.ai',
    tags={'release': 'sandbox'}
)
