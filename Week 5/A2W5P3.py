def check_triangle(side_a, side_b, side_c) -> bool:
    return (
        side_a > 0
        and side_b > 0
        and side_c > 0
        and side_a < side_b + side_c
        and side_b < side_a + side_c
        and side_c < side_a + side_b
    )


def main():
    side_a = float(input("Side A: "))
    side_b = float(input("Side B: "))
    side_c = float(input("Side C: "))

    if check_triangle(side_a, side_b, side_c):
        print("Possible triangle")
    else:
        print("Impossible triangle")


if __name__ == "__main__":
    main()
