<template>
  <MainLayout>
    <component
      :is="projectSteps"
      @next-step="nextStep"
      @save-project="saveProject"
    />
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import {action, get} from '@store/constants'

import MainLayout from '@components/layout/MainLayout'
import CreateProjectFirstStep from '@components/project/CreateProjectFirstStep'
import CreateProjectSecondStep from '@components/project/CreateProjectSecondStep'

export default {
  name: 'CreateProjectScreen',
  components: {
    MainLayout,
    CreateProjectFirstStep,
    CreateProjectSecondStep,
  },
  data() {
    return {
      isNextStep: false,
    }
  },
  computed: {
    ...mapState(['newProject']),
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
    projectSteps() {
      return this.isNextStep
        ? 'CreateProjectSecondStep'
        : 'CreateProjectFirstStep'
    },
  },
  methods: {
    ...mapActions([action.UPDATE_NEW_PROJECT, action.CREATE_PROJECT]),
    async updateProject(projectInformation) {
      await this[action.UPDATE_NEW_PROJECT](projectInformation)
    },
    async createProject(projectInformation) {
      await this[action.CREATE_PROJECT](projectInformation)
    },
    nextStep(nameProject, workspace, chanelType) {
      this.loading = true
      this.updateProject({
        title: nameProject,
        note: 'text',
        workspace: workspace,
        ...chanelType,
      })
      this.isNextStep = !this.isNextStep
    },
    saveProject() {
      this.loading = true
      this.createProject({
        ...this.newProject,
        creator: 1,
      })
      this.$router.push({
        name: 'Home',
      })
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
