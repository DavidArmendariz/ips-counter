# Web requests

## Local development

To start local development, run in the terminal:

```bash
docker-compose up -d
```

Now you are ready to go to `http://localhost:5000/` to see the app working.

If you want to stop the container, run in the terminal:

```bash
docker-compose down
```

## Endpoints

There are three endpoints:

- `/`: If you enter to this path, your IP will be stored in memory.
- `/top`: Here, you will find the top IPs by frequency.
- `/clear`: By hitting this endpoint, you will be clearing all IPs and their frequencies.

## Tests

To run the tests, run the following command in your terminal:

```bash
docker exec web-requests python -m unittest discover
```

## How does the code work?

I use two data structures: a dictionary and a min heap. The dictionary has the following structure:

```python
{
    "ip1": {"count": 1, "index_in_heap": 0},
    "ip2": {"count": 2, "index_in_heap": 1},
    ...
}
```

That is, the keys of the dictionary are the ips and the values are a nested dictionary with a `count` property and a `index_in_heap` property. By choosing a dictionary, we can increment the count of IPs in constant time, i.e. `O(1)`.

In the min heap, that we can represent as a list of tuples in Python, I save two pieces of data in each of these tuples: the count and the IP. Thus, the min heap looks like this:

```python
[(5, "127.0.0.1"), (10, "127.0.0.2"), ...]
```

Each time we record a new IP, we first check if the IP is in the frequencies dictionary. If it is, we increase the count by `1`, else we set the count to `1` and the `index_in_heap` to `-1`.

If the `index_in_heap` of the IP is `-1`, we check if the heap is not yet full. If this is true, we push an element into the heap. Else, we check if the count is greater than the minimum element in the min heap (which is the root node). If this is true, we pop the minimum element and push the current IP with its count. We make sure that the previous minimum element has `index_in_heap` equal to `-1` again in the frequencies dictionary.

If the `index_in_heap` of the IP is not `-1`, we need to modify the node with index `index_in_heap` in the min heap with the latest count. This could alter the min heap, because now this node could have a count greater than the counts of the children. Thus, we need to heapify the list of tuples again. This has a time complexity of `O(k)`, **but could have been done better if we simply delete the node (this takes `O(log k)`) and then insert a new node (again, in the worst case, this would take `O(log k)`)**.

Finally, we have to readjust the `index_in_heap` in the frequencies dictionary only for the IPs present in the min heap. This also takes `O(k)`.

So, the overall complexity of storing a new IP is `O(k)`.

For getting the IPs, we just traverse the min heap, which should take `O(k)`.

And for clearing the IPs frequency and min heap, we just set the frequencies dictionary to an empty dictionary and the min heap to an empty list, so the time complexity is `O(1)`.

## Why did I choose this approach?

The first thing that came to my mind was to only use a dictionary (or hash map). But then, I have the problem of finding the top `K` IPs. I would have to traverse the whole dictionary and that would not be efficient. The dictionary or hash map is great for increasing the count, but for tracking the IPs count, I needed another data structure and that would be a min heap.

## What other approaches did you decide not to pursue?

Trying to store the counts as indexes of an array and the element of the array as the IP. This would also work, because I could take the last `K` elements of the array, but would take a huge amount of memory if the counts are big.

## What is the runtime complexity of each function?

- `store_ip`: `O(k)`
- `get_top_k_ips`: `O(k)`
- `clear_data`: `O(1)`

`k` is the number of top IPs we want to show. The reasons are explained in the fisrt question.
