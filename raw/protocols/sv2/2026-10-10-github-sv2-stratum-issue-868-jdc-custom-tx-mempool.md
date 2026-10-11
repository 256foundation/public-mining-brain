# SRI issue #868 — Custom transactions from JDC removed from mempool during update (closed, 30 comments)

> Source: https://github.com/stratum-mining/stratum/issues/868
> Collected: 2026-10-10
> Published: see body
> Registry ID: sv2-repo

NUM: 868 STATE: closed CREATED: 2024-04-23T18:15:45Z CLOSED: 2024-09-04T13:36:03Z COMMENTS: 30
TITLE: Custom transactions from JDC removed from mempool during update
LABELS: 

### What does this PR do?
- Closes #840 
- It reads transactions from the jds mempool and the node's mempool, compares them and adds them to the new mempool that is updated. In cases where the txids are unknown it adds the fat transactions to the updated mempool as well.
- To prevent an overflow, old fat transactions are cleared before a new minning job is declared
### TOP COMMENTS #868

--- @0xciph3r (2024-08-03T13:20:47Z):
> hey @NonsoAmadi10 what's the status here?
> 
> do you need any input or help unblocking anything?

@plebhash , @jbesraa told me to rebase and update the branch that he would help with outstanding issues. I think that was why I halted. Other than that I intended on closing the opened conversation here. I have time this month to work here

--- @plebhash (2024-08-05T13:34:17Z):
> > hey @NonsoAmadi10 what's the status here?
> > do you need any input or help unblocking anything?
> 
> @plebhash , @jbesraa told me to rebase and update the branch that he would help with outstanding issues. I think that was why I halted. Other than that I intended on closing the opened conversation here. I have time this month to work here

thanks for the update!

@jbesraa is busy with other activities, so I'll help you with this PR

I'll take a couple of days to study the entire PR history and then I'll get back to you 

--- @0xciph3r (2024-08-13T15:16:29Z):
@plebhash @lorbax @jbesraa @Fi3 @Shourya742. I have taken the feedback from previous unresolved conversations and a huge help from @plebhash commit. Here is what I did:

Optimize clear_declared_mining_job function

- Move mempool lock outside the loop to reduce contention
- Compare old and new mining jobs to avoid unnecessary removals( as @Fi suggested)
- Modify transaction counters in-place for better efficiency(thank you @plebhash)
- Remove unnecessary cloning and HashMap operations
- Improve error handling and logging

I don't know if what I did addressed it or if it has introduced added complexity. I would welcome your feedback


--- @rrybarczyk (2024-09-04T13:36:03Z):
Thank you so much for the work here, but right now our plan is to refactor the `roles` completely and we want to avoid large `roles` PR's as it will eventually be refactored again. We will work on this once we have the proper integration test framework to test it in #1138.
