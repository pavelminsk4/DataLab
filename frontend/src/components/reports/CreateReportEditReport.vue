<template>
  <div class="add-widgets-button">
    <BaseButton @click="saveReport">
      <AddWidgetsIcon />
      <span>Add widgets</span>
    </BaseButton>
  </div>

  <div class="report-widgets-view"></div>

  <footer class="create-reports__footer">
    <BaseButton @click="saveReport">
      <SaveIcon />
      <span>Save Report</span>
    </BaseButton>
  </footer>
</template>

<script>
// import {action} from '@store/constants'
import AddWidgetsIcon from '@/components/icons/AddWidgetsIcon'
import SaveIcon from '@/components/icons/SaveIcon'

import BaseButton from '@/components/common/BaseButton'

export default {
  name: 'CreateReportEditReport',
  components: {AddWidgetsIcon, BaseButton, SaveIcon},
  methods: {
    saveReport() {
      this.$router.push({name: ''})

      console.log()
    },
  },
}
</script>

<style lang="scss" scoped>
.add-widgets-button {
  display: flex;
  justify-content: flex-end;
}

.report-widgets-view {
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;
  padding: 32px;
  margin-top: 20px;

  background-color: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: var(--border-radius);
}
</style>
