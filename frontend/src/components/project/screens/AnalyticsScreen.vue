<template>
  <div v-if="currentProject">
    <WidgetsModal v-if="isOpenWidgetsModal" @close="toggleWidgetsModal" />

    <NavigationBar
      v-if="currentProject"
      :title="currentProject.title"
      :hint="'Search by keywords and phrases '"
      :is-show-button="false"
    />

    <div class="navigation-bar">
      <BaseButton class="button" @click="toggleWidgetsModal">
        <PlusIcon class="icon" />
        Add Widgets
      </BaseButton>
    </div>
    <WidgetsView :project-id="currentProject.id" />
  </div>
</template>

<script>
import NavigationBar from '@/components/navigation/NavigationBar'
import WidgetsView from '@/components/widgets/WidgetsView'
import BaseButton from '@/components/buttons/BaseButton'
import PlusIcon from '@/components/icons/PlusIcon'
import WidgetsModal from '@/components/modals/WidgetsModal'

export default {
  name: 'AnalyticsScreen',
  components: {WidgetsModal, PlusIcon, BaseButton, WidgetsView, NavigationBar},
  props: {
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
  data() {
    return {
      isOpenWidgetsModal: false,
    }
  },
  methods: {
    toggleWidgetsModal() {
      this.isOpenWidgetsModal = !this.isOpenWidgetsModal
    },
  },
}
</script>

<style lang="scss" scoped>
.navigation-bar {
  display: flex;
  justify-content: flex-end;

  margin-top: 30px;

  .button {
    width: 155px;

    .icon {
      margin-right: 10px;
    }
  }
}
</style>
