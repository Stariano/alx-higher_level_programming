#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Insert node based on the n variable
 * @head: The head node
 * @n : data that should be inside the node
 * Return: The nodes after edition
 */
listint_t *insert_node(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *temp, *temp2;

	temp = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL || n < temp->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (temp->next->n <= n)
		{
			temp = temp->next;
			if (temp->next == NULL)
			break;
		}
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
