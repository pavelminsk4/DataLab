<template>
  <MainLayout>
    <component
      :is="projectSteps"
      :member="member"
      @next-step="nextStep"
      @save-project="saveProject"
      @create-project-step="createWorkspace"
    />
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import {action, get} from '@store/constants'

import MainLayout from '@components/layout/MainLayout'
import CreateWorkspace from '@/components/project/CreateWorkspace'
import CreateProjectFirstStep from '@components/project/CreateProjectFirstStep'
import CreateProjectSecondStep from '@components/project/CreateProjectSecondStep'

export default {
  name: 'CreateProjectScreen',
  components: {
    MainLayout,
    CreateWorkspace,
    CreateProjectFirstStep,
    CreateProjectSecondStep,
  },
  data() {
    return {
      step: 1,
      title: '',
      description: '',
      members: [],
    }
  },
  computed: {
    ...mapState(['newProject']),
    ...mapGetters({
      workspaces: get.WORKSPACES,
      member: get.USER_ID,
    }),
    projectSteps() {
      if (this.step === 2) {
        return 'CreateProjectFirstStep'
      } else if (this.step === 3) {
        return 'CreateProjectSecondStep'
      }
      return 'CreateWorkspace'
    },
  },
  async created() {
    await this[action.GET_USER_INFORMATION]()
  },
  methods: {
    ...mapActions([
      action.UPDATE_NEW_PROJECT,
      action.CREATE_PROJECT,
      action.CREATE_WORKSPACE,
      action.GET_WORKSPACES,
      action.GET_USER_INFORMATION,
    ]),
    async updateProject(projectInformation) {
      await this[action.UPDATE_NEW_PROJECT](projectInformation)
    },
    async createProject(projectInformation) {
      await this[action.CREATE_PROJECT](projectInformation)
    },
    async createWorkspace(title, description, members) {
      try {
        this.loading = true
        this.title = title
        this.description = description
        this.members = members
        this.step = 2
      } catch (error) {
        this.loading = false
      }
    },
    nextStep(nameProject, chanelType) {
      this.loading = true
      this.updateProject({
        title: nameProject,
        note: 'text',
        ...chanelType,
      })
      this.step = 3
    },
    async saveProject() {
      this.loading = true
      this[action.CREATE_WORKSPACE]({
        title: this.title,
        description: this.description,
        members: this.members,
        projects: [{...this.newProject, keywords: 'test', creator: 1}],
      })
      this.$router.push({
        name: 'Home',
      })
      await this[action.GET_WORKSPACES]()
    },
  },
}
</script>

<style lang="scss" scoped>
.back-button {
  cursor: pointer;

  color: var(--secondary-text-color);
}

.arrow-back {
  margin-right: 6px;
}

.title {
  margin: 5px 0 2px;

  color: var(--primary-text-color);

  font-size: 36px;
}

.create-project-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.progress-bar-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.progress-bar {
  display: flex;
  align-items: center;

  margin-right: 40px;
}

.progress-item {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 24px;
  height: 24px;

  border-radius: 100%;
  border: 1px solid var(--primary-button-color);
  box-shadow: 0 0 3px var(--box-shadow-color);

  color: var(--primary-text-color);
  background-color: var(--primary-bg-color);
}

.progress-line {
  width: 34px;
  height: 2px;

  background-color: var(--progress-line);
}

.next-button {
  width: 114px;
}

.hint {
  color: var(--secondary-text-color);

  font-size: 14px;
}
</style>
