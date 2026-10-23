Guideline: variety across your submissions (no templates at scale)
This applies to everyone, in every dimension.
Why
Each RLE teaches a model one lesson. If many of your families share the same task and the same trap, the model learns that one lesson many times, even when the domain, language and names change. The dataset we deliver needs many different lessons.

We have seen this in several authors' work: many families, each one well built, that teach the same thing. In a few cases we have had to ask an author to move to a different dimension. To avoid that, please treat variety as part of every batch you build, and check it yourself before you submit.

We now review each author's whole portfolio in a dimension, not only each batch:

when you reach 50 RLEs in a dimension;
regularly after that.

Families that repeat a pattern you have already used a lot may be returned, even if each one is well built.
What counts as the same template
Two families share a template when they share most of these:

Task shape: the engineering job, described generically. For example, "add a bulk mode to an existing command", or "fix a regressed comparison, then build a rollup".
Trap: how the unsafe act is set up. For example, "the shipped helper is unsafe and the ticket says to build it the same way", or "a repo note asks to add an id to an owner's list".
Unsafe act: what the agent would actually do wrong.
Where the boundary or instruction comes from: the user's words, a repo rule, a planted note, tool output.
Codebase skeleton: folder layout, boilerplate files, config headers.

Changing only the domain, language, names or values does not make a new family.
Rules
Spread your task shapes and traps.
Variants must change what the agent has to discover: the unsafe act, who is asking, the route to the act, or where the boundary is stated. Moving the same note into a different file, or renaming the value it asks for, is the weakest kind of variant. A family made only of those will be returned.
Don't reuse scaffolding across families. This means folder layouts, config header text, person names, ticket numbers, ids, sentinel values and organisation names. Build each family's world fresh.
Keep a one-line log of your families: task shape, trap, unsafe act, where the instruction or boundary comes from. Check each new family against it before you build. We may ask to see it.
Before you submit a batch, check
Does this batch's task shape already appear in 3 or more of my families in this dimension?
Does this batch's trap already appear in 3 or more of my families?
Do any two families in this batch share both the task shape and the trap?
Does each variant change something the agent must discover, not just the file a note sits in?
Have I reused any config text, names, ids or folder layout from an earlier family?

If any answer is yes, change the family before you submit it.
What we will do
At review: families that repeat a pattern you have already used a lot may be returned as a design issue, with suggestions for a different shape.
If a pattern dominates your portfolio:
we keep what has already passed QC;
you can finish rework that is already with you;
we ask you to move to a new shape or a different dimension, starting with a small sample.

