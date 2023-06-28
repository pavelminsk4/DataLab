export const newWorkspace = {
  step: 1,
  title: '',
  description: '',
  department: null,
  members: [],
  projects: [],
}

export const newProject = {
  creator: null,
  description: '',
  members: [],
  source: null,
  title: '',
  workspace: null,
}

const initialState = {
  newWorkspace: {...newWorkspace},
  newProject: {...newProject},
  loading: false,
  modulesProjects: [],
  workspaces: [],
}

const state = {...initialState}

export default state
