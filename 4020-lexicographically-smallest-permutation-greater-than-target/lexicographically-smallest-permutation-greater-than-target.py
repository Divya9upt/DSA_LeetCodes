class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        a = sorted(s)
        n = len(a)

        # Find the smallest permutation of s
        # that is greater than target.
        #
        # We construct it from right to left.

        for i in range(n - 1, -1, -1):

            # Try to keep target[0:i] same
            prefix = target[:i]

            # Count characters needed after prefix
            remaining = list(s)

            possible = True

            for ch in prefix:
                if ch in remaining:
                    remaining.remove(ch)
                else:
                    possible = False
                    break

            if not possible:
                continue

            # Find smallest character > target[i]
            candidates = sorted(
                ch for ch in remaining
                if ch > target[i]
            )

            if candidates:
                ch = candidates[0]
                remaining.remove(ch)

                return prefix + ch + ''.join(sorted(remaining))

        return ""