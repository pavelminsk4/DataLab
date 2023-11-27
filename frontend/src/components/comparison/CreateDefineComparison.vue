<template>
  <div class="wrapper">
    <form class="form">
      <section class="form__module">
        <CustomText tag="span" text="Module" />
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
        <CustomText
          tag="h4"
          text="Select which projects to compare (2 or 3 projects)"
        />
        <CustomText tag="span" text="Projects" />
        <DivWithError
          :has-error="!!errors.project"
          :error-message="errors.project"
        >
          <DropdownWithSelect
            v-model="projects.project"
            :workspaces="currentWorkspaces"
            name="Project"
            class="select"
          />
        </DivWithError>
        <CustomText tag="span" text="Competitor project" />
        <DivWithError
          :has-error="!!errors.projectToCompare"
          :error-message="errors.projectToCompare"
        >
          <DropdownWithSelect
            v-model="projects.projectToCompare"
            :workspaces="currentWorkspaces"
            name="ProjectToCompare"
            class="select"
          />
        </DivWithError>
        <CustomText tag="span" text="Competitor project" />
        <CustomText tag="span" text="Optional" class="hint" />
        <DropdownWithSelect
          v-model="projects.projectToCompareOptional"
          :workspaces="currentWorkspaces"
          name="ProjectToCompareOptional"
          :class="[
            'select',
            (!projects.project.id || !projects.projectToCompare.id) &&
              'disabled',
          ]"
        />
      </section>
    </form>
    <BaseButton :is-disabled="errors.disableBtn" @click="saveWorkspace">
      <SaveIcon color="#ffffff" class="save-icon" />
      <CustomText tag="span" text="Save Project" />
    </BaseButton>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import CustomText from '@components/CustomText'
import DivWithError from '@components/DivWithError'
import DropdownWithSelect from '@components/DropdownWithSelect'
import BaseRadio from '@components/BaseRadio'
import OnlineIcon from '@components/icons/OnlineIcon'
import SocialIcon from '@components/icons/SocialIcon'
import BaseButton from '@components/common/BaseButton'
import SaveIcon from '@components/icons/SaveIcon'

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
    CustomText,
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
      errors: {
        project: null,
        projectToCompare: null,
        disableBtn: false,
      },
    }
  },
  computed: {
    ...mapState(['modulesProjects', 'newWorkspace', 'newProject']),
    currentWorkspaces() {
      if (isAllFieldsEmpty(this.modulesProjects)) return []

      return this.modulesProjects[this.currentModule]
        .filter((workspace) => !isAllFieldsEmpty(workspace))
        .map((workspace) => {
          const workspaceName = Object.keys(workspace)[0]
          const projects = workspace[workspaceName].filter((currentProject) => {
            return !Object.values(this.projects).find(
              (selectedProject) => selectedProject?.id === currentProject.id
            )
          })
          return {[workspaceName]: projects}
        })
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
  watch: {
    'projects.project'(newValue) {
      if (newValue && this.errors.project) {
        this.errors.project = null
      }
    },
    'projects.projectToCompare'(newValue) {
      if (newValue && this.errors.projectToCompare) {
        this.errors.projectToCompare = null
      }
    },
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
    validation() {
      this.errors.project = isAllFieldsEmpty(this.projects.project)
        ? 'You have to choose project'
        : null
      this.errors.projectToCompare = isAllFieldsEmpty(
        this.projects.projectToCompare
      )
        ? 'You have to choose project to compare'
        : null

      this.errors.disableBtn = !!(
        this.errors.project || this.errors.projectToCompare
      )

      return !this.errors.project && !this.errors.projectToCompare
    },
    saveWorkspace() {
      const isValid = this.validation()
      if (!isValid) return

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
  margin-bottom: 30px;

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

.disabled {
  opacity: 0.5;
  pointer-events: none;
}
</style>
