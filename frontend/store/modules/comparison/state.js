const initialState = {
  newWorkspace: {
    step: 1,
    title: '',
    description: '',
    department: null,
    members: [],
    projects: [],
  },
  newProject: null,
  workspaces: [],
  loading: false,
}

const state = {...initialState}

export default state
