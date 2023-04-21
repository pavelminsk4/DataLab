<template>
  <div class="wrapper-input">
    <BaseInput
      v-model="searchText"
      :isSearch="true"
      placeholder="Search projects..."
      label=" "
    />
  </div>
  <div class="wrapper scroll">
    <ProjectsTableWithModules v-model="selectedProjects" :projects="projects" />
  </div>
  <footer class="create-reports__footer">
    <ButtonWithArrow :is-disabled="isDisableNextBtn" @click="nextStep">
      <span>Next</span>
    </ButtonWithArrow>
  </footer>
</template>

<script>
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
const {mapActions: mapSocialActions} = createNamespacedHelpers('social')

import ProjectsTableWithModules from '@/components/ProjectsTableWithModules'
import BaseInput from '@components/common/BaseInput'

import createAlertMixin from '@/lib/mixins/create-alerts.js'

export default {
  name: 'CreateAlertAddProject',
  components: {ProjectsTableWithModules, BaseInput},
  mixins: [createAlertMixin],
  data() {
    return {
      selectedProjects: [],
      searchText: '',
    }
  },
  computed: {
    ...mapGetters({projects: get.ALL_PROJECTS}),
    isDisableNextBtn() {
      return !this.selectedProjects.length
    },
  },
  created() {
    this.getOnlineProjects()
    this.getSocialProjects()
  },
  methods: {
    ...mapActions({getOnlineProjects: action.GET_PROJECTS}),
    ...mapSocialActions({getSocialProjects: action.GET_PROJECTS}),
    nextStep() {
      this[action.UPDATE_NEW_ALERT]({
        step: 1,
        projects: this.selectedProjects,
      })
      this.$router.push({name: 'Alerts'})
    },
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  height: calc(100% - 250px);
}

.wrapper-input {
  max-width: 30%;

  margin: 40px 0 20px 0;
}
</style>
