#BST
from django.db import models


class TrigramTreeNode(models.Model):
    trigram = models.CharField(max_length=3)
    left = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='left_child')
    right = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='right_child')


class YourModel(models.Model):
    data = models.CharField(max_length=255)


# utils.py
def create_trigram_tree(data_list):
    root = None

    for data in data_list:
        trigrams = [data[i:i + 3] for i in range(len(data) - 2)]
        for trigram in trigrams:
            root = insert_trigram(root, trigram)

    return root


def insert_trigram(node, trigram):
    if node is None:
        return TrigramTreeNode(trigram=trigram)

    if trigram < node.trigram:
        node.left = insert_trigram(node.left, trigram)
    elif trigram > node.trigram:
        node.right = insert_trigram(node.right, trigram)

    return node


def find_trigram(node, trigram):
    if node is None:
        return False

    if trigram == node.trigram:
        return True
    elif trigram < node.trigram:
        return find_trigram(node.left, trigram)
    else:
        return find_trigram(node.right, trigram)


def trigram_similarity(str1, str2):
    trigrams_str1 = set([str1[i:i + 3] for i in range(len(str1) - 2)])

    common_trigrams = 0
    root = create_trigram_tree([str2])

    for trigram in trigrams_str1:
        if find_trigram(root, trigram):
            common_trigrams += 1

    total_trigrams = len(trigrams_str1) + len(set([str2[i:i + 3] for i in range(len(str2) - 2)]))
    similarity = common_trigrams / total_trigrams if total_trigrams > 0 else 0

    return similarity