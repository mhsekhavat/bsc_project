* our work is a light sanity check library (app) for django

* Sanity Checks
** Base class Test
** action wrapper
** test harvester => all_tests
      in initialization of application, it should collect all tests

* Metrics
** coverage = # hit sanity check (given() == True and when() == True): makes us superior to contracts! (Mehran promised he will remember what this means)

* Optimization: 
** prune duplicate/satisfied-a-lot/already-checked tests

* Test Generation phase
** User-defined scenarios
** Production
** Model-based behavior (markov chain)
** Maximizing coverage (hard?)

* Report
** we implement a django project for edu, as proof of concept
** thesis

* About concurrency:
If the system begins a transaction for each request, it's possible to run sanity checks concurrently without facing 
race conditions.

* Other:
** Security?
** Relation with Aspect Oriented Design?
** Relation with Mutational Testing?
** vs. Design by Contract

