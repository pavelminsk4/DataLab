<template>
  <BaseModal modal-frame-style="width: 36vw; height: auto;">
    <div class="title">Report</div>

    <div class="radio-wrapper">
      <BaseRadio
        v-for="(item, index) in reportTypes"
        :key="item + index"
        v-model="selectedValue"
        :id="item + index"
        :checked="item"
        :value="item"
        :label="item"
        class="radio-btn"
      />
    </div>

    <BaseButton @click="openReportSettings" class="button">Next</BaseButton>
  </BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal'
import BaseRadio from '@/components/BaseRadio'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'DownloadReportModal',
  components: {BaseButton, BaseRadio, BaseModal},
  data() {
    return {
      reportTypes: ['Instant', 'Regular'],
      selectedValue: '',
      isRegularReport: false,
    }
  },
  methods: {
    openReportSettings() {
      if (this.selectedValue === 'Instant') {
        this.$emit('open-instant-template')
      }

      if (this.selectedValue === 'Regular') {
        this.$router.push({
          name: 'Reports',
        })
      }
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

.radio-wrapper {
  display: flex;
  flex-wrap: wrap;

  margin: 10px 0 40px;
}

.radio-btn {
  margin: 0 25px 8px 0;
}

.button {
  width: 113px;
  float: right;
}
</style>

<style>
.additional-key > .input-tag {
  margin-bottom: 10px;
}
</style>
