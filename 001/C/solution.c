#include <stdio.h>

int		resolve(void)
{
	int sum = 0;

	for (int i = 1; i < 1000; ++i)
		if (i % 3 == 0 || i % 5 == 0)
			sum += i;
	return (sum);
}

int		main(void)
{
	printf("%d\n", resolve());
	return (0);
}
