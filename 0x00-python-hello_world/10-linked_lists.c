#include "lists.h"
#include <stdio.h>

/**
 * add_nodeint - A function that adds a node at the beginning of listint_t list
 * @head: A double pointer to the start of the list
 * @n: An integer to be included in the node
 *
 * Return: Address of the new element or NULL if not success
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	else
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
}

/**
 * print_listint - Function that prints listint_t list
 * @h: A pointer to the start of the list
 *
 * Return: Number of nodes in the list
 */

size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;

	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * free_listint - Function that frees listint_t list
 * @head: A pointer to the start of the list
 */

void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
