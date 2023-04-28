const initialAlert = {
  step: 1,
  title: '',
  description: '',
  user: [],
  department: null,
  creator: null,
  alert_condition: '',
  triggered_on_every_n_new_posts: '',
  how_many_posts_to_send: '',
}

const alertsState = {
  alerts: [],
  newAlert: {...initialAlert},
}

export default alertsState
export {initialAlert}
