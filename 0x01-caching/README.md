# Project: 0x01. Caching

## Overview

This project covers various caching mechanisms and their implementations. Caching is a technique used to store frequently accessed data in a temporary storage area to improve performance and reduce latency. The project includes implementations of different cache replacement policies such as FIFO, LIFO, LRU, MRU, and LFU.

## Resources

### Read or watch

* [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_(FIFO))
* [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_(LIFO))
* [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU))
* [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_(MRU))
* [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_(LFU))

## Learning Objectives

### General

* What a caching system is
* What FIFO means
* What LIFO means
* What LRU means
* What MRU means
* What LFU means
* What the purpose of a caching system
* What limits a caching system have

## Tasks

| Task                | File                                   | Description                                                                 |
|---------------------|----------------------------------------|-----------------------------------------------------------------------------|
| 0. Basic dictionary | [0-basic_cache.py](./0-basic_cache.py) | Implement a basic caching system using a dictionary.                        |
| 1. FIFO caching     | [1-fifo_cache.py](./1-fifo_cache.py)   | Implement a caching system with a First-In-First-Out (FIFO) eviction policy.|
| 2. LIFO Caching     | [2-lifo_cache.py](./2-lifo_cache.py)   | Implement a caching system with a Last-In-First-Out (LIFO) eviction policy. |
| 3. LRU Caching      | [3-lru_cache.py](./3-lru_cache.py)     | Implement a caching system with a Least Recently Used (LRU) eviction policy.|
| 4. MRU Caching      | [4-mru_cache.py](./4-mru_cache.py)     | Implement a caching system with a Most Recently Used (MRU) eviction policy. |
| 5. LFU Caching      | [100-lfu_cache.py](./100-lfu_cache.py) | Implement a caching system with a Least Frequently Used (LFU) eviction policy.|
