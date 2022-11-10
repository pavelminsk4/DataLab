<template>
  <BaseModal modal-frame-style="width: 36vw; height: auto;">
    <div class="title">Report</div>

    <div class="radio-wrapper">
      <BaseRadio
        v-for="(item, index) in reportTypes"
        :key="item + index"
        :checked="item"
        :value="selectedValue"
        class="radio-btn"
        @change="changeValue(item)"
      >
        <template #default>
          <div class="not-check"><CheckRadioIcon class="check-icon" /></div>
          {{ item }}
          <div v-if="item === 'Regular'" class="not-available">
            Not available now!
          </div>
        </template>
      </BaseRadio>
    </div>

    <BaseButton @click="openReportSettings" class="button">Next</BaseButton>
  </BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal'
import BaseRadio from '@/components/BaseRadio'
import BaseButton from '@/components/buttons/BaseButton'

import CheckRadioIcon from '@/components/icons/CheckRadioIcon'

export default {
  name: 'DownloadReportModal',
  components: {BaseButton, BaseRadio, BaseModal, CheckRadioIcon},
  data() {
    return {
      reportTypes: ['Instant', 'Regular'],
      selectedValue: '',
      isRegularReport: false,
    }
  },
  methods: {
    changeValue(newValue) {
      this.selectedValue = newValue
    },
    openReportSettings() {
      if (this.selectedValue === 'Instant') {
        this.$emit('open-instant-template')
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

.not-check {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  margin-right: 7px;
  border: 1px solid var(--secondary-text-color);
  border-radius: 50px;
  cursor: pointer;
}

.check-icon {
  display: none;
}

.radio-btn {
  display: flex;

  margin: 0 25px 8px 0;

  color: var(--primary-text-color);

  cursor: pointer;
}

.button {
  width: 113px;
  float: right;
}

.not-available {
  margin-left: 5px;
  color: var(--negative-status);
}
</style>

<style>
.additional-key > .input-tag {
  margin-bottom: 10px;
}

.radio-wrapper > .selected {
  background: none;
}

.radio-wrapper > .selected .not-check {
  border: none;
  background: var(--primary-button-color);
}

.radio-wrapper > .selected .check-icon {
  display: flex;
}
</style>
