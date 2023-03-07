#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *loop;

	loop = list;
	if (list == NULL || list->next == NULL)
		return (0);

	while (loop != NULL)
	{
		loop = loop->next;
		if (loop == list)
			return (1);
	}
	return (0);
}
