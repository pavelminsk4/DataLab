<template>
  <div :class="['chips-wrapper', chipsType.toLowerCase()]">
    <component :is="`${chipsType}Icon`" />
    <span>{{ title }}</span>
  </div>
</template>

<script>
import {capitalizeFirstLetter} from '@/lib/utilities'

import maleIcon from '@/components/icons/MaleIcon'
import femaleIcon from '@/components/icons/FemaleIcon'
import SocialIcon from '@/components/icons/SocialIcon'
import OnlineIcon from '@/components/icons/OnlineIcon'
import TVRadioIcon from '@/components/icons/TVRadioIcon'

export default {
  name: 'BaseChips',
  components: {maleIcon, femaleIcon, SocialIcon, OnlineIcon, TVRadioIcon},
  props: {
    chipsType: {type: String, required: true},
  },
  computed: {
    title() {
      return this.currTitle(this.chipsType)
    },
  },
  methods: {
    capitalizeFirstLetter,
    currTitle(chipsTitle) {
      switch (chipsTitle) {
        case 'TVRadio':
          return 'TV&Radio'
        case 'Social':
          return 'Social Media'
        default:
          return capitalizeFirstLetter(chipsTitle)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.chips-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;

  width: fit-content;
  height: 100%;
  gap: 5px;
  padding: 6px 8px;

  border-radius: 2px 12px 12px 2px;

  overflow: hidden;
  &:not(:last-child) {
    margin-right: 6px;
  }
}

.male {
  background: var(--neutral-secondary-color);
}
.female {
  background: #ffe3e8;
}

.undefined {
  background: var(--background-additional-color);
}

.online {
  background: var(--background-additional-color);
}
.social {
  background: var(--background-additional-color);
}
.tvradio {
  background: var(--background-additional-color);
}
</style>
