<template>
  <MainLayout>
    <div v-if="workspace" class="create-project-wrapper">
      <div>
        <h1 class="title">Title</h1>
        <span class="hint">
          Select the project you want to work on or create a new search
        </span>

        <div class="sort-wrapper">
          <span class="hint">Sort by</span>
          <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>
        </div>
      </div>

      <BaseButton class="create-new-button"> Create new project </BaseButton>
    </div>

    <BaseTable :values="workspace?.projects" />
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import SortIcon from '@components/icons/SortIcon'

import MainLayout from '@components/layout/MainLayout'
import BaseButton from '@components/buttons/BaseButton'
import BaseTable from '@components/workspace/ProjectsTable'

export default {
  name: 'WorkspaceScreen',
  components: {BaseTable, MainLayout, BaseButton, SortIcon},
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    workspace() {
      return this.workspaces.find((el) => el.id === +this.workspaceId)
    },
  },
  async created() {
    await this[action.GET_WORKSPACES]()
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
  },
}
</script>

<style lang="scss" scoped>
.create-project-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.title {
  margin: 0 0 8px;

  color: var(--primary-text-color);

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 42px;
}

.hint {
  color: var(--secondary-text-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}

.sort-wrapper {
  display: flex;

  margin: 34px 0 22px;

  color: var(--primary-text-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}

.sort-option {
  display: flex;
  align-items: center;

  margin-left: 15px;
}

.sort-icon {
  margin-left: 7px;
}

.create-new-button {
  width: 178px;
}
</style>
