import random

class UtilityService:

    def slot_true_chance(self, p: float) -> bool:
        """確率pでtrueを返す

        Args:
            p (float): 確率

        Returns:
            bool: 判定の成否
        """
        rng = random.random()
        return p > rng
