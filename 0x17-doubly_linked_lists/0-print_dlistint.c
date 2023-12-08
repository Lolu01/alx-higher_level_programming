#include "lists.h"

/**
 * print_distinct - Prints all the elements of a distinct_t list.
 *
 * @h: Head of the list.
 *
 * Return: The number of nodes.
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t node_count = 0;

	if (h == NULL)
		return (node_count);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		node_count++;
		h = h->next;
	}

	return (node_count);
}
