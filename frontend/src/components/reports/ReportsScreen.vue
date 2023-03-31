<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock
        title="Reports"
        description="Set up and manage reports"
        :back-page="{name: 'main page', routName: 'MainView'}"
      />

      <BaseButton @click="$emit('create-report')">
        Create new report
      </BaseButton>
    </div>

    <template v-if="reports.length">
      <div class="sort-wrapper">
        <span class="hint">Sort by</span>
        <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>

        <BaseInput
          v-model="search"
          placeholder="Search users..."
          :isSearch="true"
        />
      </div>

      <div class="list-wrapper scroll">
        <ListOfEntities
          :values="filteredProjects"
          :members="reports?.members"
          @go-to-entity="goToReport"
          @delete-entity="deleteReport"
        />
      </div>
    </template>

    <div v-else class="no-reports-wrapper">
      <img src="@/assets/reports/no-reports.svg" alt="No reports image" />
      <div>No reports created &#x1F4E8;</div>
    </div>
  </MainLayout>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import SortIcon from '@components/icons/SortIcon'

import BaseButton from '@/components/common/BaseButton'
import BaseInput from '@/components/common/BaseInput'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ListOfEntities from '@/components/ListOfEntities'

export default {
  name: 'ReportsScreen',
  components: {
    BaseButton,
    BaseInput,
    MainLayout,
    MainLayoutTitleBlock,
    ListOfEntities,
    SortIcon,
  },
  props: {
    reports: {type: Array, default: () => []},
  },
  data() {
    return {
      search: '',
    }
  },
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
      isLoading: get.LOADING,
    }),
    filteredProjects() {
      //change
      if (!this.search) return this.reports?.projects
      return this.reports?.projects.filter((project) =>
        project.title.toLowerCase().includes(this.search.toLowerCase())
      )
    },
  },
  methods: {
    goToReport(reportId) {
      this.$emit('open-report', reportId)
    },
    deleteReport(id) {
      //change
      return id
    },
  },
}
</script>

<style lang="scss" scoped>
.content-header {
  display: flex;
  justify-content: space-between;
}

.online-icon {
  width: 20px;
  height: 20px;
}

.sort-wrapper {
  display: flex;
  align-items: center;

  margin-bottom: 22px;
}

.hint {
  color: var(--typography-secondary-color);
}

.sort-option {
  flex-grow: 1;
  display: flex;
  align-items: center;

  margin-left: 15px;
}

.sort-icon {
  margin-left: 7px;
}

.list-wrapper {
  height: calc(100% - 200px);
}

.no-reports-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;
}
</style>
