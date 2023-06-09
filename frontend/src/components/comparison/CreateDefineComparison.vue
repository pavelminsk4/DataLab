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
          v-model="project"
          :workspaces="currentWorkspaces"
          name="Project"
        />
        <span>Competitor project</span>
        <DropdownWithSelect
          v-model="projectToCompare"
          :workspaces="currentWorkspaces"
          name="ProjectToCompare"
        />
        <span>Competitor project(optional)</span>
        <DropdownWithSelect
          v-model="projectToCompareOptional"
          :workspaces="currentWorkspaces"
          name="ProjectToCompareOptional"
        />
      </section>
    </form>
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

const {mapActions: mapComparisonActions, mapState: mapComparisonState} =
  createNamespacedHelpers('comparison')

export default {
  name: 'CreateDefineComparison',
  components: {BaseRadio, DropdownWithSelect, OnlineIcon, SocialIcon},
  data() {
    return {
      currentModule: 'Online',
      project: {},
      projectToCompare: {},
      projectToCompareOptional: {},
    }
  },
  computed: {
    ...mapComparisonState(['workspaces']),
    currentWorkspaces() {
      if (isAllFieldsEmpty(this.workspaces)) return []
      return this.workspaces[this.currentModule]
    },
    currentModuleProxy: {
      get() {
        return this.currentModule
      },
      set(val) {
        this.currentModule = val
        this.project = {}
        this.projectToCompare = {}
        this.projectToCompareOptional = {}
      },
    },
  },
  created() {
    if (isAllFieldsEmpty(this.workspaces)) this[action.GET_WORKSPACES]()

    this.radioBtns = [
      {label: 'Online', value: 'Online'},
      {label: 'Social', value: 'Social'},
    ]
  },
  methods: {
    ...mapComparisonActions([action.GET_WORKSPACES]),
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
}
.icon {
  height: 16px;
  width: 16px;
  padding: 2px;

  border-radius: 2px;
}
</style>
