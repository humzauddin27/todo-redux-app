let nextTodoId = 0
export const addTodo = (text) => ({
  type: 'ADD_TODO',
  id: nextTodoId++,
  text
})

export const setVisibilityFilter = (filter) => ({
  type: 'SET_VISIBILITY_FILTER',
  filter
})

export const toggleTodo = (id) => ({
  type: 'TOGGLE_TODO',
  id
})


//backend stuff
export const fetchTodos = () => ({
	type: 'FETCH_TODOS'
})

export const todosFetchedSuccess = () => ({
	type: 'FETCH_SUCCESS'
})

export const todosFetchedFailure = () => ({
	type: 'FETCH_FAILURE'
})

export const recieveTodos = () => ({
	type: 'RECIEVE_TODOS',
	items
})
