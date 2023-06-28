<template>
  <div class="wrapper">
    <form class="form">
      <section class="form__module">
        <span>Module</span>
        <base-radio
          v-for="item in radioBtns"
          v-model="currentModuleProxy"
          :key="item.value"
          :value="item.value"
          :id="item.value"
          :label="item.label"
          class="grow"
        >
          <component :is="item.label + 'Icon'" class="icon" />
        </base-radio>
      </section>
      <section class="form__projects" v-if="currentWorkspaces.length">
        <h4>Select which projects to compare (2 or 3 projects)</h4>
        <span>Project</span>
        <DropdownWithSelect
          v-model="projects.project"
          :workspaces="currentWorkspaces"
          name="Project"
        />
        <span>Competitor project</span>
        <DropdownWithSelect
          v-model="projects.projectToCompare"
          :workspaces="currentWorkspaces"
          name="ProjectToCompare"
        />
        <span>Competitor project(optional)</span>
        <DropdownWithSelect
          v-model="projects.projectToCompareOptional"
          :workspaces="currentWorkspaces"
          name="ProjectToCompareOptional"
        />
      </section>
    </form>
    <BaseButton
      :is-disabled="
        isAllFieldsEmpty(projects.project) ||
        isAllFieldsEmpty(projects.projectToCompare)
      "
      @click="saveWorkspace"
    >
      <SaveIcon class="save-icon" /> Save Project
    </BaseButton>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {isAllFieldsEmpty} from '@/lib/utilities'

import BaseRadio from '@/components/BaseRadio'
import OnlineIcon from '@components/icons/OnlineIcon'
import SocialIcon from '@components/icons/SocialIcon'
import DropdownWithSelect from '@components/DropdownWithSelect'
import BaseButton from '@/components/common/BaseButton'
import SaveIcon from '@/components/icons/SaveIcon'

const {mapActions, mapState} = createNamespacedHelpers('comparison')

export default {
  name: 'CreateDefineComparison',
  components: {
    BaseButton,
    BaseRadio,
    DropdownWithSelect,
    OnlineIcon,
    SaveIcon,
    SocialIcon,
  },
  props: {
    workspaceId: {type: String, default: ''},
  },
  data() {
    return {
      currentModule: 'Online',
      projects: {
        project: {},
        projectToCompare: {},
        projectToCompareOptional: {},
      },
    }
  },
  computed: {
    ...mapState(['modulesProjects', 'newWorkspace', 'newProject']),
    currentWorkspaces() {
      if (isAllFieldsEmpty(this.modulesProjects)) return []

      return this.modulesProjects[this.currentModule].filter(
        (workspace) => !isAllFieldsEmpty(workspace)
      )
    },
    currentModuleProxy: {
      get() {
        return this.currentModule
      },
      set(val) {
        this.currentModule = val
        this.projects.project = {}
        this.projects.projectToCompare = {}
        this.projects.projectToCompareOptional = {}
      },
    },
  },
  created() {
    if (isAllFieldsEmpty(this.modulesProjects)) this[action.GET_PROJECTS]()

    this.radioBtns = [
      {label: 'Online', value: 'Online'},
      {label: 'Social', value: 'Social'},
    ]
  },
  methods: {
    isAllFieldsEmpty,
    ...mapActions([
      action.GET_PROJECTS,
      action.CREATE_WORKSPACE,
      action.UPDATE_WORKSPACE,
      action.UPDATE_NEW_COMPARISON_WORKSPACE,
    ]),
    saveWorkspace() {
      const projects = []
      const module =
        this.currentModule === 'Online' ? 'Project' : 'ProjectSocial'

      for (const projectKey in this.projects) {
        if (this.projects[projectKey].id) {
          projects.push({
            module_type: module,
            module_project_id: this.projects[projectKey].id,
          })
        }
      }

      const workspace = {
        title: this.newWorkspace.title,
        description: this.newWorkspace.description,
        department: this.newWorkspace.departament,
        members: this.newWorkspace.members,
        cmpr_workspace_projects: [
          {
            title: this.newProject.title,
            members: this.newProject.members,
            cmpr_items: projects,
          },
        ],
      }

      if (this.workspaceId === 'new') this[action.CREATE_WORKSPACE](workspace)
      else {
        this[action.UPDATE_WORKSPACE]({
          workspaceId: this.workspaceId,
          workspace: {
            ...workspace.cmpr_workspace_projects[0],
            creator: this.newProject.creater,
            note: '',
            workspace: null,
            members: [],
          },
        })
      }

      this[action.UPDATE_NEW_COMPARISON_WORKSPACE]()

      this.$router.push({
        name: 'Comparison',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.form {
  display: flex;
  flex-direction: column;

  margin-bottom: 20px;
  gap: 40px;
  &__module {
    display: flex;
    flex-direction: column;
    gap: 12px;

    .grow {
      width: 100%;
    }
  }

  &__projects {
    display: flex;
    flex-direction: column;

    span {
      margin-top: 10px;
    }

    div {
      margin-top: 5px;
    }
  }
}
.icon {
  height: 16px;
  width: 16px;
  padding: 2px;

  border-radius: 2px;
}
</style>
