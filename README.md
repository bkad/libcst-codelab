Getting started with libCST
===

Installation
---

First, install the requirements:

    pip install -r requirements.txt

Then make sure you can run the example.
This is a simple visitor that takes all instances of the value `1` and changes it to `9`.

    python -m libcst.tool codemod one_visitor.OneVisitor example/transform_me.py

Take a look at the results with `git diff`.
Peek at the transformer in `example/one_visitor.py`.
Visitors give you a hook into the parser's output and allow you to transform your code.

Initialization
---

A couple of quick notes about the `.libcst.codemod.yaml` file in this directory:

* The initialization file is necessary to run libCST.
* It is created by running `python -m libcst.codemod initialize`
* Your custom transformers should be add to the `modules` section.
  They've been pre-added for the sake of this codelab,
  so you won't need to make changes to the init file.

Step 1
---

Our goal is to write a transformer that changes `Optional[x]` to `x | None`.
The first step would be to figure out how libCST parses both the code we want to transform and the code we
want the result to look like.

To that end, I've created a file that has just two lines in it:

```python
Optional[x]
x | None
```

Run `python -m libcst.tool print example/print_me.py` to look at the nodes we need to match,
and how they should look after we've transformed them.

After running `print`, you'll see two Nodes in their respective statements.
One is the node we want to transform:

```python
Subscript(
    value=Name(
        value="Optional",
    ),
    slice=[
        SubscriptElement(
            slice=Index(
                value=Name(
                    value="x",
                ),
            ),
        ),
    ],
)
```

The other is the node we want our resulting code to look like:

```python
BinaryOperation(
    left=Name(
        value="x",
    ),
    operator=BitOr(),
    right=Name(
        value="None",
    ),
)
```

Based on this, implement the transformer in `step1/step1_optional_visitor.py`.
Refer to `example/one_visitor.py` as a model.
If you get stuck, you can refer to the solution in `step1_solution/step1_example_solution.py`.

To run your solution:

    python -m libcst.tool codemod step1_optional_visitor.Optional step1/transform_me.py

Verify that no uses of `Optional` remain!

Step 2
---

Our goal now is to match against multiple patterns and
transform uses of `Optional[x]` and `typing.Optional[x]` to `x | None`.

You can form compound matches using bit-wise boolean operators like:

```python
libcst.matchers.Integer("1") | libcst.matchers.Integer("57")
```

This example would match `1` OR `57`.

Create your solution in `step2/step2_optional_visitor.py`.
If you get stuck, check out the solution in `step2_solution/step2_example_solution.py`.

Run your solution with:

    python -m libcst.tool codemod step2_optional_visitor.Optional step2/transform_me.py
