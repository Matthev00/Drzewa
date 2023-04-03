import sys
import gc
import time
import matplotlib.pyplot as plt
from random import randint
from BST import BSTNode
from avl import AVLTree
from nums import number_pool
from copy import deepcopy


N = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]


def plot(bst_times, avl_times, title):
    plt.plot(N, bst_times, color='r', label='BST')
    plt.plot(N, avl_times, color='b', label='AVL')
    plt.xlabel("Number count")
    plt.ylabel("Time")
    plt.title(title)
    plt.legend()
    plt.savefig(title + '.png')


def build_bst(nums):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    bst = BSTNode()
    for n in nums:
        bst.insert(n)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def build_avl(nums):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    avl = AVLTree()
    root = None
    for n in nums:
        root = avl.insert_node(root, n)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def create_build_plot():
    bst_build_times = []
    avl_build_times = []
    for id in N:
        bst_build_times.append(build_bst(number_pool[:id]))
        avl_build_times.append(build_avl(number_pool[:id]))

    plot(bst_build_times, avl_build_times, "Building trees")


def search_bst(bst, nums):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for n in nums:
        bst.exists(n)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def search_avl(avl, root, nums):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for n in nums:
        avl.exists(n, root)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def create_search_plot():
    bst_search_times = []
    avl_search_times = []

    # build bst
    bst = BSTNode()
    for n in number_pool:
        bst.insert(n)

    # build avl
    avl = AVLTree()
    root = None
    for n in number_pool:
        root = avl.insert_node(root, n)

    for id in N:
        bst_search_times.append(search_bst(bst, number_pool[:id]))
        avl_search_times.append(search_avl(avl, root, number_pool[:id]))

    plot(bst_search_times, avl_search_times, "Searching in trees")


def remove_bst(bst, nums):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for n in nums:
        bst.delete(n)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def create_bst_removing_plot():
    bst_removing_times = []
    # build bst
    bst = BSTNode()
    for n in number_pool:
        bst.insert(n)
    for id in N:
        bst_removing_times.append(remove_bst(deepcopy(bst), number_pool[:id]))

    # plot
    plt.plot(N, bst_removing_times, color='r', label='BST')
    plt.xlabel("Number count")
    plt.ylabel("Time")
    plt.title("Removing in BST")
    plt.legend()
    plt.savefig('Removing in BST.png')


def main():
    sys.setrecursionlimit(1000000)
    # generating this takes minutes, importing pregenerated from nums.py
    # numbers_pool = [randint(1, 30000) for _ in range(10000)]
    # uncomment to create plot
    # create_build_plot()
    # create_search_plot()
    # create_bst_removing_plot()


if __name__ == '__main__':
    main()
