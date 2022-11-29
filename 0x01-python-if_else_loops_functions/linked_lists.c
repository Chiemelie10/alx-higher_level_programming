#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * print_listint - A function that prints listint_t list
 * @h: A pointer to the start of the list
 *
 * Return: The number of nodes in the list
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n = 0;

	current = h;

	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint_end - A function that adds a node at the end of listint_t list
 * @head: a double pointer to the start of the list
 * @n: integer to be added to the new node
 *
 * Return: The address of the new node if success, otherwise NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *temp;
	listint_t *new_node;

	temp = *head;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;
	else
	{
		while (temp->next != NULL)
			temp = temp->next;
		temp->next = new_node;
	}

	return (new_node);
}

/**
 * free_listint - Frees a listint_t list
 * @head: a pointer to the start of the list to be freed
 *
 * Return: void
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
