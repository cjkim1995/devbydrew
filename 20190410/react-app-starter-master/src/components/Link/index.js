import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';

import styles from './styles.module.scss';

export default function Link({ href, children, target, rel, underline, className }) {
  let _rel;
  if (target === '_blank' && (!rel || !rel.includes('noopener noreferrer'))) {
    _rel = `${rel} noopener noreferrer`;
  } else {
    _rel = rel;
  }

  return (
    <a href={href} target={target} rel={_rel} className={classNames(className, {[styles.noUnderline]: !underline })}>
      {children}
    </a>
  );
}

Link.propTypes = {
  href: PropTypes.string.isRequired,
  children: PropTypes.node.isRequired,
  target: PropTypes.string,
  rel: PropTypes.string,
  underline: PropTypes.bool,
  className: PropTypes.string,
};

Link.defaultProps = {
  target: undefined,
  rel: undefined,
  underline: true,
  className: undefined,
};
