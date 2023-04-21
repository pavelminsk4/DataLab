<template>
  <form class="form" @submit.prevent="nextStep">
    <BaseInput
      v-model="triggerFrequency"
      label="Trigger on evey N new posts"
      placeholder="Number of post"
      class="input-name"
    />

    <BaseInput
      v-model="triggerPostCount"
      label="How many post to send"
      placeholder="Number of post"
      class="input-name"
    />
    <div class="form__trigger">
      <span>Send notification if trigger condition is not met in a week</span>
      <BaseSwitcher :value="triggerInWeek" @input="switchTrigger" />
    </div>

    <footer>
      <ButtonWithArrow
        :is-disabled="!triggerFrequency"
        type="submit"
        class="next-button"
      >
        <span>Next</span>
      </ButtonWithArrow>
    </footer>
  </form>
</template>

<script>
import {action} from '@store/constants'

import BaseSwitcher from '@/components/BaseSwitcher.vue'
import BaseInput from '@/components/common/BaseInput'

import createAlertMixin from '@/lib/mixins/create-alerts.js'

export default {
  name: 'SetAlertTrigger',
  components: {BaseSwitcher, BaseInput},
  mixins: [createAlertMixin],
  data() {
    return {
      triggerFrequency: '',
      triggerPostCount: '',
      triggerInWeek: false,
    }
  },
  methods: {
    switchTrigger() {
      this.triggerInWeek = !this.triggerInWeek
    },
    nextStep() {
      const nextStep = 3
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_ALERT]({
        step: nextStep,
        triggerInWeek: this.triggerInWeek,
        triggered_on_every_n_new_posts: this.triggerFrequency,
        how_many_posts_to_send: this.triggerPostCount,
      })

      this.$router.push({name: nextStepName})
    },
  },
}
</script>

<style lang="scss" scoped>
.form {
  display: flex;
  flex-direction: column;

  padding: 40px 0px;
  gap: 30px;

  width: 65%;

  @media (max-width: 1100px) {
    width: 100%;
  }

  &__trigger {
    display: flex;
    flex-wrap: nowrap;
    gap: 10px;

    padding: 14px 12px;

    border: 1px solid #dee0e3;
    border-radius: 8px;
  }
}
</style>
