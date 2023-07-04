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
        <DivWithError
          :has-error="errors.project.hasError"
          :error-message="errors.project.errorMessage"
        >
          <DropdownWithSelect
            v-model="projects.project"
            :workspaces="currentWorkspaces"
            name="Project"
            class="select"
          />
        </DivWithError>
        <span>Competitor project</span>
        <DivWithError
          :has-error="errors.projectToCompare.hasError"
          :error-message="errors.projectToCompare.errorMessage"
        >
          <DropdownWithSelect
            v-model="projects.projectToCompare"
            :workspaces="currentWorkspaces"
            name="ProjectToCompare"
            class="select"
          />
        </DivWithError>
        <span>Competitor project <span class="hint">Optional</span></span>
        <DropdownWithSelect
          v-model="projects.projectToCompareOptional"
          :workspaces="currentWorkspaces"
          name="ProjectToCompareOptional"
          class="select"
        />
      </section>
    </form>
    <BaseButton :is-disabled="errors.disableBtn" @click="saveWorkspace">
      <SaveIcon class="save-icon" /> Save Project
    </BaseButton>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {isAllFieldsEmpty} from '@/lib/utilities'

import DivWithError from '@/components/DivWithError'
import DropdownWithSelect from '@components/DropdownWithSelect'
import BaseRadio from '@/components/BaseRadio'
import OnlineIcon from '@components/icons/OnlineIcon'
import SocialIcon from '@components/icons/SocialIcon'
import BaseButton from '@/components/common/BaseButton'
import SaveIcon from '@/components/icons/SaveIcon'

const {mapActions, mapState} = createNamespacedHelpers('comparison')

export default {
  name: 'CreateDefineComparison',
  components: {
    DivWithError,
    DropdownWithSelect,
    BaseButton,
    BaseRadio,
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
    errors() {
      const project = isAllFieldsEmpty(this.projects.project)
        ? {hasError: true, errorMessage: 'You have to choose project'}
        : {hasError: false}
      const projectToCompare = isAllFieldsEmpty(this.projects.projectToCompare)
        ? {
            hasError: true,
            errorMessage: 'You have to choose project to compare',
          }
        : {hasError: false}
      const sameProjects =
        this.projects.project.id === this.projects.projectToCompare.id &&
        !(
          isAllFieldsEmpty(this.projects.project) &&
          isAllFieldsEmpty(this.projects.projectToCompare)
        )

      if (sameProjects) {
        projectToCompare.hasError = true
        projectToCompare.errorMessage = 'You cant compare the same project'
      }
      const disableBtn = project.hasError || projectToCompare.hasError

      return {
        project,
        projectToCompare,
        disableBtn,
      }
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
      action.GET_WORKSPACES,
      action.CREATE_WORKSPACE,
      action.UPDATE_WORKSPACES_PROJECTS,
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
        department: this.newWorkspace.department,
        members: this.newWorkspace.members,
        cmpr_workspace_projects: [
          {
            title: this.newProject.title,
            note: this.newProject.description,
            members: this.newProject.members,
            cmpr_items: projects,
            creator: this.newProject.creator,
            workspace: this.workspaceId === 'new' ? null : this.workspaceId,
          },
        ],
      }

      if (this.workspaceId === 'new') {
        this[action.CREATE_WORKSPACE](workspace)
        this.$router.push({
          name: 'Comparison',
        })
      } else {
        this[action.UPDATE_WORKSPACES_PROJECTS]({
          data: {
            ...workspace.cmpr_workspace_projects[0],
          },
        })
        this.$router.push({
          name: 'ComparisonWorkspace',
          params: this.$route.params.workspaceId,
        })
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.form {
  display: flex;
  flex-direction: column;

  gap: 40px;

  &__module {
    display: flex;
    flex-direction: column;
    gap: 12px;

    .grow {
      width: 100%;
    }
  }

  &__error {
    border: 1px solid var(--negative-status);
    border-radius: 10px;
  }

  &__projects {
    display: flex;
    flex-direction: column;

    div {
      border-radius: 8px;
    }

    .select {
      height: 40px;
    }
    .no-error {
      visibility: hidden;
      font-size: 12px;
      color: transparent;

      transition: all 0.5s;
    }

    .error {
      visibility: visible;
      color: var(--primary-color);
    }

    .hint {
      font-style: italic;
      color: var(--primary-color);
    }

    span {
      margin-top: 10px;
    }
  }
}
.icon {
  height: 16px;
  width: 16px;
  padding: 2px;

  border-radius: 2px;
}

.base-button {
  margin-top: 5px;
}
</style>
