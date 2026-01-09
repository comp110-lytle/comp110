---
title: Practice Memory Diagram
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

```
    def apply_discounts(order_amounts: list[float]) -> list[float]:
        index: int = 0
        counter: int = 0
        discounted_amounts: list[float] = []

        while index < len(order_amounts):
            amount: float = order_amounts[index]

            if amount > 50:
                discount = 0.10
            else:
                discount = 0

            discounted_amount = amount * (1 - discount)
            discounted_amounts.append(discounted_amount)

            counter += 1
            index += 1

        print(f"Total orders processed: {counter}")
        return discounted_amounts

    def main() -> None:
        order_amounts: list[float] = [45.0, 75.0, 150.0, 30.0]
        discounted_amounts: list[float] = apply_discounts(order_amounts)
        print(discounted_amounts)

    if __name__ == "__main__":
        main()
```

# Solution

<img class="img-fluid" src="/static/mem-diags/discount-soln.jpg" alt="Image Description Here"  />

## Video
*(Video Coming Soon)*

## Image Description
*(Coming Soon)*