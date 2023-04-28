// Alerts
const alertsState = {
  alerts: [],
  newAlert: {
    step: 1,
    title: '',
    description: '',
    user: [],
    department: null,
    creator: null,
    alert_condition: '',
    triggered_on_every_n_new_posts: '',
    how_many_posts_to_send: '',
  },
}

export default alertsState
