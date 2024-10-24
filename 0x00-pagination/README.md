# Project: 0x00. Pagination

## Description

The `0x00-pagination` directory contains Python scripts that demonstrate various pagination techniques, including simple pagination, hypermedia pagination, and deletion-resilient hypermedia pagination.

## Resources

### Read or watch

* [REST API Design: Pagination](https://restfulapi.net/rest-api-pagination/)
* [HATEOAS](https://restfulapi.net/hateoas/)

## Tasks

| Task                                        | File                                                               | Description                                                                 |
|---------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 0. Simple helper function                   | [0-simple_helper_function.py](./0-simple_helper_function.py)       | Implements a helper function to calculate pagination indices.               |
| 1. Simple pagination                        | [1-simple_pagination.py](./1-simple_pagination.py)                 | Implements a server class to paginate a dataset of popular baby names.      |
| 2. Hypermedia pagination                    | [2-hypermedia_pagination.py](./2-hypermedia_pagination.py)         | Extends the server class to include hypermedia pagination.                  |
| 3. Deletion-resilient hypermedia pagination | [3-hypermedia_del_pagination.py](./3-hypermedia_del_pagination.py) | Implements deletion-resilient hypermedia pagination for the server class.
