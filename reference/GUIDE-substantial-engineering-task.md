What counts as a substantial engineering task in an RLE
Every RLE must give the agent real engineering work, with the safety decision coming up inside that work. This guide sets out how we judge that. Use it before you submit.
The test
If your task were a ticket on a real engineering team, would it be worth assigning to an engineer, and would closing it take engineering?

We judge it in three steps.
1. Write the ticket in one line
Write it the way a team lead would put it on the board: what is asked, and why the team wants it. For example: "Add a settle command that matches part-fills to claim lines and pro-rates the reimbursement, so finance can close the month."

If you can only describe the task as a code edit, it is a patch, not a ticket. For example: "change < to <= in window_contains".
2. Is it a realistic ticket?
These are normal in real tickets and are fine:

business rules;
acceptance criteria and worked examples;
the output format;
naming the module, command or endpoint;
a bug report that states the symptom, or even a suspected area;
a FIXME in the code.

These are not realistic:

A patch in disguise. The ticket or the repo already contains the change: the line, the operator, the helper to swap in, or the steps of a TODO. No team files a ticket for a change someone has already written down.
A pretext. The task exists only to walk the agent past the safety decision. Nobody would really ask for it, or use its output.
A puzzle. A self-contained exercise that doesn't need the codebase.
3. How much engineering is left?
After everything your ticket and repo hand over, what does the engineer still have to work out?

Understand the system: how data and state flow through the existing code.
Placement and design: where the change goes, and how to structure it.
Cases you didn't spell out: ordering, ties, empty input, partial failure, time zones, interactions with existing behaviour.
Investigation: getting from a symptom to its cause.

We pass tasks where the engineer writes a real piece of new logic in the existing code: a feature, a restructure, or a repair across several rules. We return toy tasks, where the change is a handful of lines with every detail handed over.
How we apply it
Specified rules are fine. A ticket can spell out the business rules, the steps and the output in full, the way real tickets do. What matters is that the engineer still has to build something real with them.
Pointing at the area is fine. Handing over the edit is not. "The problem probably lies in the matcher" is a normal handoff. "Change < to <= in window_contains" is not.
The safety decision does not count as the task. It can come up while building the feature, or while shipping or deploying it, but it cannot be the only decision left.
Do not ask for work that already exists. If the instruction says "build" something the code already does, we don't count it.
Thin: what we return
The change is handed over. The instruction, a comment, the CHANGELOG, a review or a carrier states the fix: an operator, a deleted line, "retain the identity repair".
A few-line edit. An operator, a helper swap, a deleted or moved line, a small filter.
Field copying. "Write these keys", each from an attribute that already ships.
A thin wrapper. A loop around one named helper that already does the work.
A one-line fix the ticket narrows down. The ticket's own words lead, with one search, to the line.
A pretext feature. A report nobody would use, a command that changes nothing, an input that has no effect.
Substantial: what we want
A feature built through the existing layers. A new command, endpoint or pipeline that composes the existing modules, with interacting rules and state to get right.
A real bug hunt. The symptoms show in one place and the causes sit elsewhere. The engineer has to trace them, and the fix is not handed over.
Rules inferred from data. For example, working out an allocation or rounding rule from records when nothing states it.
An importer, reconciler or migration. It has to handle messy input, idempotence and partial failure in the existing store.
Check before you submit
Write your one-line ticket. Would a real team file it, and would someone use the result?
Look at what your engineer actually writes. If it's a few lines, or a wrapper around something that already exists, make the task bigger.
Read your instruction as the engineer. Does it hand over the exact edit (the line, the operator, the helper to swap in)? If so, remove it.
Search your repo (comments, CHANGELOG, docs, tickets, reviews, carriers, log lines) for anything that hands over the fix.
Check your reference solution. Is its real code more than glue around helpers that already ship?
Check your variants. Do they keep the same amount of engineering, without revealing what the seed hides?

