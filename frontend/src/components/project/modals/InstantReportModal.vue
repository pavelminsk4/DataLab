<template>
  <BaseModal modal-frame-style="width: 30vw; height: auto;">
    <div class="title">Template settings</div>
    <a class="button" :href="`/projects/${projectId}/reports/instantly_report`">
      Download
    </a>
  </BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal'

export default {
  name: 'InstantReportModal',
  components: {BaseModal},
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
  },
}
</script>

<style scoped>
.title {
  margin-bottom: 40px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
}

.button {
  text-decoration: none;

  padding: 10px 30px;

  background: var(--primary-button-color);
  border-radius: 8px;

  color: var(--primary-text-color);
}
</style>
