#!/usr/bin/python3
'''A module to check if all boxes can be unlocked
'''


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the lockboxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visible_boxes = set([0])
    invisible_boxes = set(boxes[0]).difference(set([0]))
    while len(invisible_boxes) > 0:
        boxIdx = invisible_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in visible_boxes:
            invisible_boxes = invisible_boxes.union(boxes[boxIdx])
            visible_boxes.add(boxIdx)
    return n == len(invisible_boxes)
