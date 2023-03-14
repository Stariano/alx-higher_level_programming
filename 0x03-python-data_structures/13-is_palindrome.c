#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

#define MAX 20

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: takes a pointer to head (the first pointer to the first node)
 * Return: 1 - If Palindrome / 0 - If nor Palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp2;

	if (*head == NULL)
		return (1);

	temp = *head;
	temp2 = *head;
	int array[MAX];
	int top = 0;

	while (temp != NULL)
	{
		array[top] = temp->n;
		top++;
		temp = temp->next;
	}

	while (temp2 != NULL)
	{
		top = top - 1;
		if (temp2->n != array[top])
			return (0);
		temp2 = temp2->next;
	}
	return (1);
}
