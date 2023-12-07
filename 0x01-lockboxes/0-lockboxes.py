#!/usr/bin/python3
'''A module to check if all boxes can be unlocked
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    available_boxes = set([0])
    unavailable_boxes = set(boxes[0]).difference(set([0]))
    while len(unavailable_boxes) > 0:
        boxIdx = unavailable_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in available_boxes:
            unavailable_boxes = unavailable_boxes.union(boxes[boxIdx])
            available_boxes.add(boxIdx)
    return n == len(available_boxes)
