from INDIGO.collision.rect_collision import collision
from INDIGO.collision.valid import check_valid_group, check_valid_resp


def sprite_sprite_collision(sprite1, sprite2, resp):
    # check for collision between sprite1 and sprite2 and then call resp
    # if they collided
    """
    EngineObject Sprite1, Sprite2 - sprites to check collision on
    func resp - response to be called upon collision
    """
    check_valid_resp(resp)
    if collision(sprite1, sprite2):
        resp(sprite1, sprite2)
    return


def sprite_group_collision(sprite, group, resp, dokill):
    # check every sprite in the group for collision with the sprite
    """
    EngineObject sprite, Group group - sprite/group to check collision on
    func resp - response to be called upon collision
    bool dokill - whether or not to kill the collided objects from the group
    """
    check_valid_resp(resp)
    check_valid_group(group)
    for obj in group:
        if collision(sprite, obj):
            resp(sprite, obj)
        if dokill:
            group.kill(obj)
    return


def group_group_collision(group1, group2, resp, dokilla, dokillb):
    # check for collision for each of the sprites with each of the other sprites
    """
    Group group1, Group group2 - groups to check collision on
    func resp - response to be called upon collision
    bool dokill, dokillb - whether or not to kill the collided objects from the group
    """
    check_valid_resp(resp)
    check_valid_group(group1)
    check_valid_group(group2)
    for obj in group1:
        for pbj in group2:
            if collision(obj, pbj):
                resp(obj, pbj)
            if dokilla:
                group1.kill(obj)
            if dokillb:
                group2.kill(pbj)
    return
