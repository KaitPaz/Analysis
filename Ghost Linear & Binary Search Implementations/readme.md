# 🔎 Linear vs. Binary Search: A Prefix-Matching Deep Dive
 
**What happens when you take two textbook search algorithms and actually
measure them against each other on ~300,000 real words?**
 
This is a hands-on exploration of algorithmic complexity: instead of just
searching for an exact match, I extended both linear and binary search to
solve a harder problem — finding the *entire contiguous range* of words
that share a given prefix — then timed both approaches head-to-head to see
whether the theory (O(n) vs. O(log n)) actually holds up in practice.
 
## 🎯 Skills demonstrated
 
| Skill | Where |
|---|---|
| **Complexity analysis** | Reasoning about why O(log n) should beat O(n) *before* measuring it |
| **Algorithm adaptation** | Extending both search strategies beyond a single-match lookup into a range-finding problem |
| **Binary search edge cases** | Handling the fact that a "found" match in binary search isn't necessarily the *first* or *last* match — solved with two independent narrowing searches |
| **Empirical benchmarking** | Using Python's `time.perf_counter()` to validate theoretical complexity with real timing data, not just intuition |
 
## 🧠 The core problem
 
Exact-match search is easy — both linear and binary search handle it in a
few lines. The real challenge here was **prefix range search**: given a
sorted word list and a prefix like `"app"`, find the start and end indices
of every word that begins with it, as a single contiguous slice.
 
**Linear approach (`linear_search_prefix`)** — walk the whole list once,
tracking the first and last index where `word.startswith(prefix)` is true.
Simple, and correct on both sorted and unsorted input, but it's O(n)
regardless of where the matches happen to live.
 
**Binary approach (`binary_search_prefix`)** — the more interesting one.
A single binary search can land on *any* word matching the prefix, not
necessarily the first or last. So this runs two independent binary
searches over the sorted list: one that keeps narrowing left every time it
finds a match (to converge on the earliest matching index), and one that
keeps narrowing right (to converge on the latest). Together they pin down
the exact boundaries of the matching range in O(log n).
 
## ⏱️ The result
 
Timing both approaches with `time.perf_counter()` on the same ~300k-word
list makes the O(n) vs. O(log n) gap concrete rather than theoretical —
binary search's advantage isn't just an asymptotic argument, it's
something you can watch happen in microseconds.
 
## 🚀 Running it
 
```bash
python3 prefix_search.py
```
 
You'll be prompted for a prefix, then see:
- The matching index range
- How long the linear approach took
- How long the binary approach took
- Every word in the matching range
Needs a `words.txt` file in the same directory — one word per line. (The
version this was built against used a ~300k-word English word list; any
sorted-on-load word list works.)
 
## 📄 Notes
 
Built to internalize *why* complexity class matters, not just recite it —
by extending both algorithms to a problem where the difference between
O(n) and O(log n) is actually visible.
 
