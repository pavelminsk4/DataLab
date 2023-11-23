<template>
  <div class="settings-container" ref="settings-wrapper">
    <div
      v-if="isOpenSettings"
      :style="`${position}: calc(100% + 8px);`"
      class="options-container"
    >
      <slot></slot>
    </div>
    <PointsIcon
      :class="['points-icon', isOpenSettings && 'active-points']"
      @click.stop="openSettings"
    />
  </div>
</template>

<script>
import PointsIcon from '@components/icons/PointsIcon'

export default {
  name: 'BaseTooltipSettings',
  components: {
    PointsIcon,
  },
  props: {
    position: {type: String, default: 'top'},
    id: {
      type: [Number, String],
      default: '',
    },
  },
  data() {
    return {
      isOpenSettings: false,
    }
  },
  created() {
    document.addEventListener('click', this.close)
  },
  methods: {
    openSettings() {
      this.isOpenSettings = !this.isOpenSettings
    },
    close({target}) {
      const selectList = document.querySelector('.settings-container')

      if (!selectList?.contains(target)) {
        this.isOpenSettings = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-container {
  position: relative;

  width: 30px;
  height: 30px;
}

.options-container {
  z-index: 3;

  position: absolute;
  right: -5px;

  display: flex;
  flex-direction: column;

  padding: 8px;

  border-radius: 4px;
  box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);
  background: var(--background-secondary-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 110%;
  white-space: nowrap;
  color: var(--typography-title-color);
}

.close-options {
  display: none;
}

.points-icon {
  z-index: 3;

  flex-shrink: 0;

  width: 30px;
  height: 30px;

  transition: all 0.3s;
  pointer-events: stroke;

  color: var(--typography-secondary-color);
}

.points-icon:hover {
  border-radius: 100%;
  background-color: var(--button-primary-color);

  color: var(--button-text-color);
}

.active-points {
  border-radius: 100%;
  background-color: var(--button-primary-color);

  color: var(--button-text-color);
}
</style>
